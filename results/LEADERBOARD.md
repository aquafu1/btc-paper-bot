# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 12:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 498 windows, 13712 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1164 | 51.2 | 49.9 | $-212.25 | -1.8% | $787.75 | -0.6 | done | can't tell from luck |
| value_ev20 | 255 | 33.7 | 35.5 | $-229.21 | -9.0% | $770.79 | -1.1 | done | can't tell from luck |
| trend_filter | 805 | 49.8 | 50.8 | $-530.71 | -6.6% | $469.29 | -1.9 | done | can't tell from luck |
| value_ev10 | 646 | 37.9 | 39.8 | $-540.56 | -8.4% | $459.44 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 1385 | 49.9 | 49.7 | $-544.41 | -3.9% | $455.59 | -1.5 | done | can't tell from luck |
| value_ev5 | 953 | 40.2 | 41.6 | $-676.78 | -7.1% | $323.22 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1385 | 50.1 | 51.5 | $-981.77 | -7.1% | $18.23 | -2.7 | done | losing for real |
| coinflip | 1985 | 50.1 | 50.7 | $-1039.93 | -5.2% | $-39.93 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1164 | 48.8 | 51.3 | $-1099.85 | -9.4% | $-99.85 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1985 | 49.7 | 51.6 | $-1484.32 | -7.5% | $-484.32 | -3.5 | done | losing for real |
| always_up | 1985 | 46.1 | 50.2 | $-2433.06 | -12.3% | $-1433.06 | -5.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3097 | 47.3 | 49.2 | $-2608.84 |
| ETH | 3430 | 48.0 | 48.7 | $-2314.35 |
| SOL | 3576 | 47.7 | 49.1 | $-2749.24 |
| XRP | 3609 | 48.4 | 48.8 | $-2100.41 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
