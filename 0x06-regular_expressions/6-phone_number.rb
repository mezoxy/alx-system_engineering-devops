#!/usr/bin/env ruby
puts ARGV[0].scan(/^[0-9]{9,9}[0-9]$/).join
#puts ARGV[0].scan(/^\d{9,9}\d$/).join
