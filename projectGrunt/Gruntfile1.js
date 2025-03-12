module.exports = function(grunt) {
    // Project configuration
    grunt.initConfig({
      concat: {
        dist: {
          src: ['src/file1.js', 'src/file2.js'], // Source files to concatenate
          dest: 'dist/output.js' // Destination file
        }
      }
    });
  
    // Load the plugin that provides the "concat" task
    grunt.loadNpmTasks('grunt-contrib-concat');
  
    // Default task(s)
    grunt.registerTask('default', ['concat']); // Register the 'concat' task as the default task
  };
  