from orator.migrations import Migration


class UpdateTeamsTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('teams') as table:
            table.string('team_id').change()
            table.string('admin').change()
            table.datetime('sign_in_time').change()
            table.string('team_name').change()
            table.string('team_image').change()
            table.string('prefecture_id').change()
            table.string('prefecture_name').change()
            table.string('city_id').change()
            table.string('city_name').change()
            table.string('line_id').change()
            table.string('line_name').change()
            table.string('station_id').change()
            table.string('station_name').change()
            table.string('gender').change()
            table.text('comment').change()
            table.string('week_id').change()
            table.string('time_id').change()
            table.string('join_status').change()
            table.datetime('game_date').change()
            table.string('purpose_id').change()
            table.string('status').change()
            table.string('feature_id').change()
            table.string('feature_name').change()
            table.string('challenge_id').change()
            table.string('send_team_id').change()
            table.string('res_team_id').change()
            table.integer('count').change()
            table.integer('avg_age').change()
            table.boolean('solicitation_flg').change()
            table.string('gym').change()
            table.string('main_place').change()
            table.text('c_comment').change()
            table.text('u_comment').change()
            table.integer('member_num').change()
            table.boolean('stray_flg').change()
            table.time('game_time_start').change()
            table.time('game_time_end').change()
            table.string('exec_type').change()
            table.string('game_status').change()
            table.string('challenge_status').change()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('teams') as table:
            # Reverse the changes made in up()
            pass