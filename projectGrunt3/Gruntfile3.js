// Multiple JS File as Output

module.exports = function (grunt) {
  grunt.initConfig({
    concat: {
      options: {
        separator: ';',
      },
      js1: {
        src: ['assets/js/file1.js', 'assets/js/file2.js'],
        dest: 'output/output1.js',
      },
      js2: {
        src: ['assets/js/file3.js', 'assets/js/file4.js'],
        dest: 'output/output2.js',
      },
    },
  });

  // Load the plugin that provides the "concat" task
  grunt.loadNpmTasks('grunt-contrib-concat');

  // Default task(s)
  grunt.registerTask('default', ['concat']);
};
