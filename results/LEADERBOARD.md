# Paper trading leaderboard (FAKE money)

**Updated Tue Nov 17, 5:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 612 windows, 16905 settled trades, 54 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1426 | 51.2 | 49.7 | $-204.41 | -1.4% | $795.59 | -0.5 | done | can't tell from luck |
| value_ev20 | 327 | 34.3 | 35.2 | $-244.70 | -7.5% | $755.30 | -1.0 | done | can't tell from luck |
| trend_filter | 973 | 50.4 | 51.0 | $-541.10 | -5.6% | $458.90 | -1.8 | done | can't tell from luck |
| value_ev10 | 788 | 38.1 | 39.4 | $-578.33 | -7.3% | $421.67 | -1.7 | done | can't tell from luck |
| value_ev5 | 1186 | 40.4 | 41.3 | $-721.34 | -6.1% | $278.66 | -1.8 | done | can't tell from luck |
| reversal_15m_0.10pct | 1728 | 50.7 | 50.9 | $-816.74 | -4.7% | $183.26 | -2.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1728 | 49.3 | 50.1 | $-957.85 | -5.5% | $42.15 | -2.3 | done | losing for real |
| coinflip | 2441 | 50.1 | 50.5 | $-1196.84 | -4.9% | $-196.84 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1426 | 48.8 | 51.3 | $-1341.79 | -9.4% | $-341.79 | -3.6 | done | losing for real |
| momentum_5m_0.00pct | 2441 | 50.4 | 51.8 | $-1548.76 | -6.3% | $-548.76 | -3.3 | done | losing for real |
| always_up | 2441 | 47.0 | 49.8 | $-2356.65 | -9.7% | $-1356.65 | -4.8 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3845 | 48.0 | 49.2 | $-2540.55 |
| ETH | 4227 | 48.0 | 48.6 | $-2742.50 |
| SOL | 4390 | 47.9 | 48.8 | $-2922.30 |
| XRP | 4443 | 48.5 | 48.6 | $-2303.16 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
