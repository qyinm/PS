defmodule Solution do
  @spec find_words_containing(words :: [String.t], x :: char) :: [integer]
  def find_words_containing(words, x) do
    x = <<x>>
    answer = for {word, idx} <- Enum.with_index(words), String.contains?(word, x) do 
            idx
        end
    answer
  end
end