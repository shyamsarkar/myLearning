module.exports = function(grunt) {
    // Project configuration
    grunt.initConfig({
      concat: {
        shyam: {
          src: ['src/file1.js', 'src/file2.js'], // Source files to concatenate
          dest: 'bootstrap/bootstrap.js' // Destination file
        }
      },
      uglify: {
        options: {
          // Uglify options
          compress: {
            drop_console: true // Remove console.* statements
          }
        },
        sarkar: {
          src: 'bootstrap/bootstrap.js', // Source file to minify
          dest: 'bootstrap/bootstrap.min.js' // Destination file
        }
      }
    });
  
    // Load Grunt plugins
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-uglify');
  
    // Define default task
    grunt.registerTask('default', ['concat', 'uglify']);
  };
  