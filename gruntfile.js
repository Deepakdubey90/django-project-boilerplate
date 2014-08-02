/**
 * Created by vinitkumar on 02/08/14.
 */

module.exports = function(grunt) {

  grunt.initConfig({
    pkg: grunt.file.readJSON('package.json'),
    concat: {
      dist: {
        src: [],
        dest: 'newco/static/newco/js/<%= pkg.name %>.add.js'
      }
    },
    uglify: {
      options: {
        banner: '/*! <%= pkg.name %> <%= grunt.template.today("dd-mm-yyyy") %> */\n'
      },
      dist: {
        files: {
          'newco/static/newco/js/<%= pkg.name %>.min.js': ['<%= concat.dist.dest %>']
        }
      }
    },
    jshint: {
      files: ['gruntfile.js', 'newco/static/newco/js/app/**/*.js'],
      ignores: ['**/*.min.js'],
      options: {
        // options here to override JSHint defaults
        globals: {
          jQuery: true,
          console: true,
          module: true,
          document: true
        }
      }
    },
    less: {
      debug: {
        src: 'newco/static/newco/css/styles.less',
        dest: 'newco/static/newco/css/styles.css'
      }
    },
    cssmin: {
      'newco/static/newco/css/styles.css': [
        'newco/static/newco/css/styles.css'
      ]
    },
    watch: {
      files: ['<%= jshint.files %>'],
      tasks: ['jshint']
    }
  });

  grunt.loadNpmTasks('grunt-contrib-uglify');
  grunt.loadNpmTasks('grunt-contrib-jshint');
  grunt.loadNpmTasks('grunt-contrib-watch');
  grunt.loadNpmTasks('grunt-contrib-concat');
  grunt.loadNpmTasks('grunt-contrib-cssmin');
  grunt.loadNpmTasks('grunt-contrib-less');
  grunt.loadNpmTasks('grunt-contrib-requirejs');

  grunt.registerTask('test', ['jshint']);
  grunt.registerTask('js', ['concat','uglify']);
  //default tasks for js files
  grunt.registerTask('default', ['jshint', 'concat', 'uglify']);
  //css compilation from less and minification
  grunt.registerTask('css', ['less', 'cssmin']);

};
