// Passing Args

module.exports = function (grunt) {
 
    grunt.registerTask('customTask1', 'A custom task example Description Here', function (args1, args2) {
        grunt.log.writeln(`args3 + args4 = ${args1+args2}`);
    });
    
    
    grunt.registerTask('customTask2', 'A custom task example Description Here', function (args3, args4) {
        grunt.log.writeln(`args3 + args4 = ${args3+args4}`);
    });


    grunt.registerTask('default', ['customTask1:1:2', 'customTask2:3:4']);
    // grunt.registerTask('runBothTasks', ['customTask1:1:2', 'customTask2:3:4']);
};



/*
grunt.task.registerTask('myTask', 'Description', function(){})

grunt.task.renameTask('oldTask', 'newTask');

var taskExists = grunt.task.exists('taskName');

grunt.task.clearQueue();

grunt.task.requires('dependencyTask');

var currentTask = grunt.task.current;

grunt.task.init([]);


grunt.task.loadTasks('path/to/tasks');

*/
