-- Exercicio 17 (insere_ordenado)

insere_ordenado :: (Num a, Ord a) => [a] -> a -> [a]
insere_ordenado [] e = [e]
insere_ordenado (c:r) e 
  |e <= c    = e : c : r 
  |otherwise = c : insere_ordenado r e

-- Exercicio 20 (mediana)

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

-- Exercicio 23 (rodar_direita)

rodar_direita :: Int -> [a] -> [a]
rodar_direita 0 lista = lista
rodar_direita n lista = rodar_direita (n - 1) (ultimoElemento lista : primeirosElementos lista)

ultimoElemento :: [a] -> a
ultimoElemento [x] = x
ultimoElemento (_:r) = ultimoElemento r

primeirosElementos :: [a] -> [a]
primeirosElementos [x] = []
primeirosElementos (c:r) = c : primeirosElementos r

-- Exercicio 32 (primo)

primo :: Int -> Bool
primo 0 = False
primo 1 = False
primo n = primoRec n (n - 1)
  where
    primoRec n 1 = True
    primoRec n d
      | n `mod` d == 0 = False
      | otherwise = primoRec n (d - 1)

-- Exercicio 33 (soma_digitos)

soma_digitos :: Int -> Int
soma_digitos 0 = 0
soma_digitos n = n `mod` 10 + soma_digitos (n `div` 10)

