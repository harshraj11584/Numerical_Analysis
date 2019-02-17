note
    description: "project3 application root class"

class
    APPLICATION

inherit
    ARGUMENTS_32

create
    make

feature {NONE} -- Initialization

    make
            -- Run application.
        require
          nothing: True
        local
            n,i,j: INTEGER
            matrix : ARRAY2[REAL]
        do
            io.read_integer
            n:=io.last_integer

            create matrix.make_filled (0, n, 2*n)

            --take input
            from i:=1 until i>n loop
                from j:=1 until j>2*n   loop
                    if j<n+1 then
                        io.read_real
                        matrix.put (io.last_real, i, j)
                    else
                        if j-n=i then
                            matrix.put (1, i, j)
                        else
                            matrix.put (0,i,j)
                        end
                    end


                    j:=j+1
                end
                i:=i+1
            end

            --uncomment to see input
            --print_matrix(matrix)

      if (n=1) then
        if (matrix.item (1,1)=0) then
          print("INVALID%N")
        else
          print((1/matrix.item (1,1)).out+"%N")
        end

      else
              --calculate_inverse
              matrix:= find_inverse(matrix)

              --see result
              print_matrix(matrix)
      end
      ensure
        nothing: True
      rescue
        print("INVALID%N")
        end

    exchange_rows(r1: INTEGER; r2: INTEGER; m: ARRAY2[REAL]) : ARRAY2[REAL]
        require
          r1>0 and r2>0 and r1<=m.height and r2<=m.height and m.height>0 and (m.height * m.height*2 = m.capacity)
        local
            i,n: INTEGER
            tmp: REAL
        do
            n:=m.height
            from i:=1 until i>2*n loop
                tmp:=m.item(r1,i)
                m.put(m.item(r2,i),r1,i)
                m.put(tmp,r2,i)
                i:=i+1
            end
            Result:=m
            ensure
              Result.height>0 and (Result.height * Result.height*2 = Result.capacity)
            rescue
        print("INVALID%N")
        end

    find_inverse(m: ARRAY2[REAL]): ARRAY2[REAL]
        require
          m.height>0 and (m.height * m.height*2 = m.capacity)
        local
            i, n, pivot_row ,k : INTEGER
            pivot_elem:REAL
            m1: ARRAY2[REAL]
        do
            n:=m.height
            m1:=m
            from i:=1 until i>n loop
                pivot_elem:=m1.item (i,i)
                if (pivot_elem/=0) then
                    m1:=subtract_row_from_all_others(i,i,m1)
                else
                    --have to get non zero below this column
                    pivot_row:=i
                    from k:=i+1 until k>n loop
                        if m1.item (i, k)/=0 then
                            pivot_row:=k
                            k:=n+1
                        end
                        k:=k+1
                    end
                    if (pivot_row=i) then
                        --no pivot found
                        --print("INVALID%N")
                        m1:=make_full_zero(m1)
                        i:=n+1
                    else
                        m1:=exchange_rows(pivot_row,i,m1)
                        m1:=subtract_row_from_all_others(i,i,m1)
                    end
                end
                i:=i+1
            end
            Result:=m1
            ensure
              Result.height>0 and (Result.height * Result.height*2 = Result.capacity)
            rescue
        print("INVALID%N")
        end

    make_full_zero(m:ARRAY2[REAL]) : ARRAY2[REAL]
        require
          m.height>0 and (m.height * m.height*2 = m.capacity)
        local
            i,j,n: INTEGER
        do
            n:=m.height
            from i:=1 until i>n loop
                from j:=1 until j>2*n loop
                    m.put (0,i,j)
                    j:=j+1
                end
                i:=i+1
            end
            Result:=m
            ensure
              Result.height>0 and (Result.height * Result.height*2 = Result.capacity) and Result.filled_with (0)
            rescue
        print("INVALID%N")
        end

    subtract_row_from_all_others(r:INTEGER;c:INTEGER;m: ARRAY2[REAL]): ARRAY2[REAL]
        require
          r>0 and c>0 and r<=m.height and c<=m.height*2 and m.height>0 and (m.height * m.height*2 = m.capacity)
        local
            i,j,n:INTEGER
            const:REAL
        do
            n:=m.height
            --making all elements in this column zero except for the one in this row
            from i:=1 until i>n loop
                if (i/=r) then
                    const:=m.item (i,c)/m.item (r,c)
                    from j:=1 until j>2*n loop
                        --m[i][j]=m[i][j]-const*m[r][j]
                        m.put (m.item (i,j)-const*m.item (r,j), i,j)
                        j:=j+1
                    end
                end
                i:=i+1
            end

            --making the first non zero element of this row 1
            const:=m.item (r,c)
            from i:=1 until i>2*n loop
                --m[r][i]=m[r][i]/const
                m.put (m.item (r,i)/const, r,i)
                i:=i+1
            end
            Result:=m
            ensure
              Result.height>0 and (Result.height * Result.height*2 = Result.capacity)
          rescue
        print("INVALID%N")
        end

    print_matrix(m: ARRAY2[REAL])
        require
          m.height>0 and (m.height * m.height*2 = m.capacity)
        local
            i,j,n,flag : INTEGER
            r: REAL
        do
            n:=m.height
            flag:=0
            --checking if invalid
            from i:=1 until i>n loop
                from j:=1 until j>2*n loop
                    if m.item (i,j)/=0 then
                        flag:=1
                        j:=2*n+1
                        i:=n+1
                    end
                    j:=j+1
                end
                i:=i+1
            end
            from i:=1 until i>n loop
                from j:=1 until j>2*n loop
                    if (m.item (i,j).is_nan) then
                      --print("YES")
                        flag:=0
                        j:=2*n+1
                        i:=n+1
                    end
                    j:=j+1
                end
                i:=i+1
            end

            if (flag/=0) then
              from i:=1 until i>n loop
                  from j:=n+1 until j>2*n loop
                      print(m.item (i, j).out+ " ")
                      j:=j+1
                  end
                  print("%N")
                  i:=i+1
              end
          else
            print("INVALID%N")
          end
          ensure
            nothing: True
          rescue
        print("INVALID%N")
        end

end