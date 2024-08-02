insere_ordenado :: (Num a, Ord a) => [a] -> a -> [a]
insere_ordenado [] e = [e]
insere_ordenado (c:r) e 
  |e <= c    = e : c : r 
  |otherwise = c : insere_ordenado r e