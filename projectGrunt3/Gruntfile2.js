// Multiple Task Configuration


module.exports = function (grunt) {
  // Project configuration
  grunt.initConfig({
    // Task configuration
    concat: {
      options: {
        separator: ';',
      },
      dist: {
        src: ['assets/js/file1.js', 'assets/js/file2.js'],
        dest: 'output/output.js',
      },
    },
    uglify: {
      options: {
        banner: '/*! <%= grunt.template.today("yyyy-mm-dd") %> */\n'
      },
      dist: {
        files: {
          'output/output.min.js': ['output/output.js']
        }
      }
    }
  });

  // Load the plugins that provide the tasks
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-uglify');

  // Default task(s)
  grunt.registerTask('default', ['concat', 'uglify']);
};
