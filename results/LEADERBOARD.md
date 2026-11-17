# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 602 windows, 16635 settled trades, 49 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 324 | 34.6 | 35.2 | $-214.70 | -6.6% | $785.30 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1408 | 51.0 | 49.6 | $-248.06 | -1.8% | $751.94 | -0.7 | done | can't tell from luck |
| value_ev10 | 777 | 38.2 | 39.4 | $-540.78 | -7.0% | $459.22 | -1.6 | done | can't tell from luck |
| trend_filter | 960 | 50.0 | 50.9 | $-586.54 | -6.1% | $413.46 | -1.9 | done | can't tell from luck |
| value_ev5 | 1166 | 40.5 | 41.2 | $-675.25 | -5.8% | $324.75 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 1696 | 51.0 | 50.9 | $-712.07 | -4.2% | $287.93 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1696 | 49.0 | 50.0 | $-1029.15 | -6.1% | $-29.15 | -2.5 | done | losing for real |
| coinflip | 2400 | 50.0 | 50.5 | $-1179.29 | -4.9% | $-179.29 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1408 | 49.0 | 51.4 | $-1287.97 | -9.1% | $-287.97 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 2400 | 50.2 | 51.8 | $-1596.76 | -6.7% | $-596.76 | -3.4 | done | losing for real |
| always_up | 2400 | 47.2 | 49.8 | $-2200.33 | -9.2% | $-1200.33 | -4.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3780 | 48.0 | 49.2 | $-2507.00 |
| ETH | 4150 | 48.0 | 48.6 | $-2719.79 |
| SOL | 4322 | 47.9 | 48.7 | $-2874.27 |
| XRP | 4383 | 48.6 | 48.6 | $-2169.85 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
