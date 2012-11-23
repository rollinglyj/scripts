#!/usr/bin/ruby -w
pid=fork do
  5.times do
    sleep 1
    puts "I am an orphan, my pid is #$$!"
  end
end

Process.wait
abort "Parent process died..."

