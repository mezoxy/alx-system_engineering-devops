#!/usr/bin/env ruby
puts ARGV[0].scan(/h[a-z]{0,1}tn/).join
# We can write also /h.{0,1}tn/
