// npm install --save-dev node-sass grunt-sass

module.exports = function (grunt) {
    const sass = require('node-sass');

    require('load-grunt-tasks')(grunt);

    grunt.initConfig({
        sass: {
            options: {
                implementation: sass,
                sourceMap: true
            },
            dist: {
                files: {
                    'output/output.css': 'assets/scss/styles.scss'
                }
            }
        }
    });

    grunt.registerTask('default', ['sass']);
};
