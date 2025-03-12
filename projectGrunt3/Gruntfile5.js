// Passing Args

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


    grunt.registerTask('customTask', 'A custom task example Description Here', function () {
        grunt.log.writeln('Running custom task...');
        grunt.log.writeln('Task completed successfully!');
    });


    grunt.registerTask('dynamicTask', function (arg) {
        // Dynamically register tasks based on conditions or configuration
        if (arg === '1') {
            grunt.log.success("Successfully Running Task");
            grunt.task.run('customTask');
        } else {
            grunt.log.warn("Failed to Run the task");
        }
    });


    // Default task(s)
    grunt.registerTask('default', ['concat','dynamicTask:1']);
};



