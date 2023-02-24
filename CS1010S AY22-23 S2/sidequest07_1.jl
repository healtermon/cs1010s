ini_p = [4//7, 2//7, 1//7, 0]
c_p = [0 2//4 1//4 1//4;
       1 0 0 0;
       1 0 0 0]
b_p = [1 0 0 0;
       0 0 2//4 2//4;
       0 1 0 0]
a_p = [1 0 0 0;
       0 1 0 0;
       0 0 0 1]
choice_p = [a_p, b_p, c_p]
p1 = ini_p

choices = [1 2 1 3 1 2 1]

chosen(choice::Int64,choice_p::Vector{Matrix{Rational{Int64}}},p::Vector{Rational{Int64}}) = sum(map((i,l) -> choice_p[i][choice,:] .* l , 1:3, p[1:3])) + [0, 0, 0, p[4]]

cho(p,choice) = chosen(choice,choice_p,p)

chosen(choices::Vector{Int64},p::Vector{Rational{Int64}}) = foldl(cho, choices, init=p)

chosen([1,2,1,3,1,2,1],ini_p)   # 1//7 3//28 3//56 39//56 
chosen([1,3,1,2,3,1,2],ini_p)   # 3//28 1//14 1//14 3//4
chosen([1,2,3,1,2,3,1],ini_p)   # 3//28 1//14 1//28 11//14
