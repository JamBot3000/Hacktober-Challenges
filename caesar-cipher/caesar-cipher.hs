import Data.Char

crypt message key = concatMap (\el -> let round = if isUpper el then 65 else 97 in [toEnum $ round + mod (key + fromEnum el) round ::Char]) message

decrypt message key = crypt message $ negate key