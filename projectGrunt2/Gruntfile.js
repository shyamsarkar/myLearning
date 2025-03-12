function myCustomTask() {
  console.log('-------------Consoling Custom Task 1-------------');
}
function myCustomTask2() {
  console.log('-------------Consoling Custom Task 2-------------');
}
function myCustomTask3() {
  console.log('-------------Consoling Custom Task 3-------------');
}



// module.exports = function(grunt) {

//   // Project configuration.
//   grunt.initConfig({
//     pkg: grunt.file.readJSON('package.json'),
//     uglify: {
//       options: {
//         banner: '/*! <%= pkg.name %> <%= grunt.template.today("yyyy-mm-dd") %> */\n'
//       },
//       build: {
//         src: 'src/<%= pkg.name %>.js',
//         dest: 'build/<%= pkg.name %>.min.js'
//       }
//     }
//   });

//   // Load the plugin that provides the "uglify" task.
//   grunt.loadNpmTasks('grunt-contrib-uglify');

//   // Default task(s).
//   grunt.registerTask('default', ['uglify']);

// };
 
module.exports = function(grunt) {
  grunt.registerTask('task1', 'My custom task description', myCustomTask);
  grunt.registerTask('task2', 'My custom task description', myCustomTask2);
  grunt.registerTask('task3', 'My custom task description', myCustomTask3);
  grunt.registerTask('all-task', ['task1', 'task2', 'task3']);
};
