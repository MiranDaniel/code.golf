(1..10000).each{|i|puts i if i%i.to_s.split("").map{|s|s.to_i}.sum<1}