// Register Custom Task

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
    },
  });



  // Load the plugin that provides the "concat" task
  grunt.loadNpmTasks('grunt-contrib-concat');


  grunt.registerTask('customTask', 'Custom Task Description Here', function () {
    grunt.log.writeln('Running custom task...');
    grunt.log.writeln('Task completed successfully!');
  });

  // Default task(s)
  grunt.registerTask('default', ['concat']);
};


/* 
write(message): Writes a message to the console without appending a newline character.

writeln(message): Writes a message to the console and appends a newline character (\n).

ok(message): Writes a success message to the console with a green "OK" prefix.

error(message): Writes an error message to the console with a red "ERROR" prefix.

warn(message): Writes a warning message to the console with a yellow "WARN" prefix.

debug(message): Writes a debug message to the console with a gray "DEBUG" prefix. This method is useful for debugging purposes and is only displayed if the --debug option is provided when running Grunt.

success(message): Writes a success message to the console with a green checkmark.

fail(message): Writes a failure message to the console with a red "FAILED" prefix. This method is used to indicate that a task has failed.
*/