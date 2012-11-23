#!/usr/bin/ruby -w
fork do
  puts "in child, pid = #$$"
  exit 99
end 
pid = Process.wait
puts "child terminated, pid = #{pid}, status = #{$?.exitstatus}"
