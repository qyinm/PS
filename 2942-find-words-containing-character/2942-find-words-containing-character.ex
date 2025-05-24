defmodule Solution do
  @spec find_words_containing(words :: [String.t], x :: char) :: [integer]
  def find_words_containing(words, x) do
    x = <<x::utf8>>
    answer = for {word, index} <- Enum.with_index(words), String.contains?(word, x) do 
            index
        end
    answer
  end
end