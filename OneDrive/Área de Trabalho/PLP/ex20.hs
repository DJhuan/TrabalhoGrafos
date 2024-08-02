ordenar :: (Ord a, Num a) => [a] -> [a]
ordenar [] = []
ordenar (c:r) = ordenar [y | y <- r, y <= c] ++ [c] ++ ordenar [y | y <- r, y > c]

mediana :: (Real a, Fractional b) => [a] -> b
mediana lista = 
    let listaOrdenada = ordenar lista
        n = comprimento listaOrdenada
    in if impar n
       then realToFrac (listaOrdenada !! (n `div` 2))
       else (realToFrac (listaOrdenada !! (n `div` 2 - 1)) + realToFrac (listaOrdenada !! (n `div` 2))) / 2

impar :: Int -> Bool
impar n = n `mod` 2 /= 0

comprimento :: [a] -> Int
comprimento [] = 0
comprimento (_:r) = 1 + comprimento r

