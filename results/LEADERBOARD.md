# Paper trading leaderboard (FAKE money)

**Updated Thu Nov 12, 8:15 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 155 windows, 3924 settled trades, 57 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| reversal_60m_0.30pct | 281 | 59.8 | 53.1 | $+277.57 | +9.9% | $1277.57 | +1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 378 | 57.1 | 52.3 | $+239.98 | +6.3% | $1239.98 | +1.3 | done | can't tell from luck |
| momentum_5m_0.00pct | 612 | 52.5 | 51.3 | $-132.48 | -2.2% | $867.52 | -0.6 | done | can't tell from luck |
| value_ev20 | 74 | 32.4 | 37.2 | $-143.54 | -19.4% | $856.46 | -1.4 | Sun 5:30 AM | too few trades (74/200) |
| coinflip | 612 | 51.0 | 50.9 | $-284.03 | -4.6% | $715.97 | -1.2 | done | can't tell from luck |
| value_ev10 | 201 | 36.8 | 40.8 | $-295.12 | -14.7% | $704.88 | -1.8 | done | can't tell from luck |
| trend_filter | 200 | 41.5 | 49.2 | $-381.61 | -19.1% | $618.39 | -2.7 | done | losing for real |
| value_ev5 | 295 | 38.0 | 42.4 | $-441.94 | -15.0% | $558.06 | -2.3 | done | losing for real |
| momentum_60m_0.30pct | 281 | 40.2 | 49.3 | $-600.16 | -21.4% | $399.84 | -3.6 | done | losing for real |
| momentum_15m_0.10pct | 378 | 42.9 | 50.0 | $-658.84 | -17.4% | $341.16 | -3.5 | done | losing for real |
| always_up | 612 | 46.1 | 50.1 | $-769.00 | -12.6% | $231.00 | -3.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 846 | 46.0 | 49.7 | $-887.46 |
| ETH | 972 | 45.6 | 48.9 | $-1090.58 |
| SOL | 1033 | 48.1 | 48.9 | $-812.83 |
| XRP | 1073 | 50.1 | 49.1 | $-398.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
