# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 9:20 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 773 windows, 21311 settled trades, 56 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 403 | 33.0 | 34.9 | $-381.45 | -9.5% | $618.55 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 2176 | 51.2 | 50.6 | $-652.29 | -3.0% | $347.71 | -1.4 | done | can't tell from luck |
| value_ev10 | 977 | 37.6 | 39.1 | $-724.62 | -7.4% | $275.38 | -1.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1800 | 49.8 | 49.6 | $-757.21 | -4.2% | $242.79 | -1.8 | done | can't tell from luck |
| trend_filter | 1250 | 49.8 | 50.8 | $-833.43 | -6.7% | $166.57 | -2.4 | done | losing for real |
| value_ev5 | 1477 | 39.9 | 41.0 | $-944.74 | -6.4% | $55.26 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 1800 | 50.2 | 51.2 | $-1186.18 | -6.6% | $-186.18 | -2.9 | done | losing for real |
| coinflip | 3084 | 50.3 | 50.3 | $-1278.05 | -4.1% | $-278.05 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 2176 | 48.8 | 50.2 | $-1447.01 | -6.6% | $-447.01 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 3084 | 51.0 | 51.6 | $-1532.14 | -5.0% | $-532.14 | -2.8 | done | losing for real |
| always_up | 3084 | 47.0 | 49.5 | $-2855.64 | -9.3% | $-1855.64 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4836 | 48.1 | 49.1 | $-2950.47 |
| ETH | 5323 | 47.9 | 48.5 | $-3630.06 |
| SOL | 5547 | 48.0 | 48.5 | $-3279.54 |
| XRP | 5605 | 48.5 | 48.4 | $-2732.68 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
