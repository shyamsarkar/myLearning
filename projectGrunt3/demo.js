module.exports = function(grunt) {
    grunt.initConfig({
      concat: {
        js: {
          src: ['src/js/*.js'],
          dest: 'dist/script.js',
        },
        css: {
          src: ['src/css/*.css'],
          dest: 'dist/style.css',
        },
      },
      uglify: {
        js: {
          src: 'dist/script.js',
          dest: 'dist/script.min.js',
        },
      },
      cssmin: {
        css: {
          src: 'dist/style.css',
          dest: 'dist/style.min.css',
        },
      },
      watch: {
        js: {
          files: ['src/js/*.js'],
          tasks: ['concat:js', 'uglify:js'],
          options: {
            livereload: true,
          },
        },
        css: {
          files: ['src/css/*.css'],
          tasks: ['concat:css', 'cssmin:css'],
          options: {
            livereload: true,
          },
        },
      },
    });
  
    // Load Grunt plugins
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
    grunt.loadNpmTasks('grunt-contrib-cssmin');
    grunt.loadNpmTasks('grunt-contrib-watch');
  
    // Register default task
    grunt.registerTask('default', ['concat', 'uglify', 'cssmin', 'watch']);
  };
  