import Data.Char

crypt message key = concatMap (\el -> let round = if isUpper el then 65 else 97 in [toEnum $ key + fromEnum el ::Char]) message

decrypt message key = crypt message $ negate key