soma_digitos :: Int -> Int
soma_digitos 0 = 0
soma_digitos n = n `mod` 10 + soma_digitos (n `div` 10)
