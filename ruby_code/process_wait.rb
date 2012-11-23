#!/usr/bin/ruby -w
3.times do
  fork do
    sleep rand(5)
  end
end


3.times do
  puts Process.wait
end
