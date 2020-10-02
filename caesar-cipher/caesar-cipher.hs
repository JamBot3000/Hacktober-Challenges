import Data.Char

crypt message key = concatMap (\el -> [toEnum $ key + fromEnum el ::Char]) message

decrypt message key = crypt message $ negate key
