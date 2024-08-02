primo :: Int -> Bool
primo 0 = False
primo 1 = False
primo n = primoRec n (n - 1)
  where
    primoRec n 1 = True
    primoRec n d
      | n `mod` d == 0 = False
      | otherwise = primoRec n (d - 1)
