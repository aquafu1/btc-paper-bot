# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 10:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 345 windows, 9255 settled trades, 59 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 184 | 37.5 | 36.6 | $-38.35 | -2.1% | $961.65 | -0.2 | Sat 6:00 PM | too few trades (184/200) |
| value_ev10 | 452 | 39.8 | 40.2 | $-215.87 | -4.8% | $784.13 | -0.8 | done | can't tell from luck |
| reversal_60m_0.30pct | 748 | 51.7 | 52.1 | $-325.87 | -4.4% | $674.13 | -1.2 | done | can't tell from luck |
| value_ev5 | 669 | 41.4 | 42.0 | $-348.22 | -5.2% | $651.78 | -1.2 | done | can't tell from luck |
| reversal_15m_0.10pct | 917 | 52.0 | 52.0 | $-374.09 | -4.1% | $625.91 | -1.3 | done | can't tell from luck |
| momentum_60m_0.30pct | 748 | 48.3 | 49.6 | $-520.93 | -7.0% | $479.07 | -1.9 | done | can't tell from luck |
| trend_filter | 504 | 46.8 | 50.2 | $-540.93 | -10.7% | $459.07 | -2.4 | done | losing for real |
| coinflip | 1372 | 50.3 | 50.8 | $-664.23 | -4.8% | $335.77 | -1.8 | done | can't tell from luck |
| momentum_15m_0.10pct | 917 | 48.0 | 49.7 | $-687.47 | -7.5% | $312.53 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1372 | 48.9 | 51.3 | $-1143.28 | -8.3% | $-143.28 | -3.2 | done | losing for real |
| always_up | 1372 | 46.7 | 50.6 | $-1551.01 | -11.3% | $-551.01 | -4.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2077 | 47.0 | 49.2 | $-1730.33 |
| ETH | 2328 | 47.5 | 48.7 | $-1708.10 |
| SOL | 2400 | 48.0 | 49.3 | $-1777.52 |
| XRP | 2450 | 48.8 | 49.1 | $-1194.29 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
