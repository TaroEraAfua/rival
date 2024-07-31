from orator.migrations import Migration


class UpdateUsersTable(Migration):

    def up(self):
        """
        Run the migrations.
        """
        with self.schema.table('users') as table:
            table.string('user_id').unique().change()
            table.string('user_name').change()
            table.string('password').change()
            table.integer('prefecture_id').unsigned().change()
            table.string('prefecture_name').change()
            table.integer('line_id').unsigned().nullable().change()
            table.string('line_name').nullable().change()
            table.integer('station_id').unsigned().nullable().change()
            table.string('station_name').nullable().change()
            table.integer('city_id').unsigned().nullable().change()
            table.string('city_name').nullable().change()
            table.date('birth_dt').change()
            table.small_integer('gender').unsigned().change()
            table.string('icon').nullable().change()
            table.integer('week_id').unsigned().nullable().change()
            table.integer('time_id').unsigned().nullable().change()
            table.integer('position_id').unsigned().nullable().change()
            table.integer('width_id').unsigned().nullable().change()
            table.integer('ex_year').unsigned().nullable().change()
            table.float('height').nullable().change()
            table.text('comment').nullable().change()

    def down(self):
        """
        Revert the migrations.
        """
        with self.schema.table('users') as table:
            # Reverse the above operations with the appropriate Orator methods
            table.drop_column('week_id')
            table.drop_column('time_id')
            table.drop_column('position_id')
            table.drop_column('width_id')
            table.drop_column('ex_year')
            table.drop_column('height')
            table.drop_column('comment')