# Run with: bundle exec ruby scripts/sync_categories.rb [--check]
# Commit the generated pages: GitHub Pages does not run custom plugins.
require "jekyll"
require "yaml"
require "fileutils"

root = File.expand_path("..", __dir__)
site = Jekyll::Site.new(Jekyll.configuration("source" => root, "safe" => true, "quiet" => true))
site.read
groups = site.categories.keys.group_by { |category| Jekyll::Utils.slugify(category) }
expected = {}
groups.sort.each do |slug, names|
  next if slug.empty?
  label = names.sort.first.delete(",").tr("-", " ")
  label = "AI safety" if slug == "ai-safety"
  label = "AI" if slug == "ai"
  label = "GPT-5" if slug == "gpt5"
  data = {"layout" => "category_index", "title" => "Topic: #{label}", "category" => label,
          "category_slug" => slug, "permalink" => "/category/#{slug}/"}
  expected["category/#{slug}.html"] = data.to_yaml + "---\n"
  redirect = {"layout" => "category_redirect", "title" => "Topic: #{label}", "category" => label,
              "permalink" => "/categories/#{slug}/", "redirect_to" => "/category/#{slug}/"}
  expected["categories/#{slug}.html"] = redirect.to_yaml + "---\n"
end
stale = expected.keys.select do |path|
  !File.exist?(File.join(root, path)) || File.read(File.join(root, path)) != expected[path]
end
if ARGV.include?("--check")
  abort "Category pages need updating: #{stale.join(', ')}" unless stale.empty?
  puts "All #{groups.length} category routes and their aliases are current."
else
  expected.each do |path, content|
    destination = File.join(root, path)
    FileUtils.mkdir_p(File.dirname(destination))
    File.write(destination, content)
  end
  puts "Wrote #{expected.length} category pages and aliases."
end
