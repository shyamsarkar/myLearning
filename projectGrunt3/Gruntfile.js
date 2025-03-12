// A Basic Configuration with Grunt


module.exports = function (grunt) {
  grunt.initConfig({
    // Task configuration
    concat: {
      options: {
        separator: ';',
      },
      dist: {
        src: ['assets/js/file1.js', 'assets/js/file2.js', 'assets/js/file3.js', 'assets/js/file4.js'],
        dest: 'output/output.js',
      },
    },
  });

  // Load the plugin that provides the "concat" task
  grunt.loadNpmTasks('grunt-contrib-concat');

  // Default task(s)
  grunt.registerTask('default', ['concat']);
};
