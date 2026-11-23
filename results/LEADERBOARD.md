# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 6:00 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1192 windows, 32932 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 643 | 34.8 | 35.3 | $-378.79 | -5.9% | $621.21 | -1.1 | done | can't tell from luck |
| value_ev10 | 1569 | 38.6 | 39.2 | $-804.19 | -5.1% | $195.81 | -1.7 | done | can't tell from luck |
| reversal_15m_0.10pct | 3297 | 50.8 | 50.3 | $-1063.73 | -3.2% | $-63.73 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 2764 | 49.6 | 49.4 | $-1208.22 | -4.4% | $-208.22 | -2.3 | done | losing for real |
| value_ev5 | 2374 | 40.3 | 41.1 | $-1292.33 | -5.4% | $-292.33 | -2.2 | done | losing for real |
| trend_filter | 1944 | 48.8 | 50.5 | $-1622.80 | -8.3% | $-622.80 | -3.8 | done | losing for real |
| reversal_60m_0.30pct | 2764 | 50.4 | 51.1 | $-1711.96 | -6.2% | $-711.96 | -3.3 | done | losing for real |
| momentum_15m_0.10pct | 3297 | 49.2 | 50.3 | $-2048.31 | -6.2% | $-1048.31 | -3.6 | done | losing for real |
| coinflip | 4760 | 50.1 | 50.2 | $-2117.00 | -4.4% | $-1117.00 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4760 | 50.1 | 51.4 | $-3037.43 | -6.4% | $-2037.43 | -4.5 | done | losing for real |
| always_up | 4760 | 47.9 | 49.3 | $-3437.61 | -7.2% | $-2437.61 | -5.0 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7561 | 48.2 | 48.9 | $-4200.72 |
| ETH | 8167 | 48.0 | 48.4 | $-5046.84 |
| SOL | 8571 | 48.2 | 48.4 | $-4388.62 |
| XRP | 8633 | 48.1 | 48.2 | $-5086.18 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
