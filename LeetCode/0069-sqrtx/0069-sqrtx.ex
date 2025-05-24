defmodule Solution do
  @spec my_sqrt(x :: integer) :: integer
  def my_sqrt(x) do
    sqrt = :math.sqrt(x)
    answer = trunc(sqrt)
    answer
  end
end