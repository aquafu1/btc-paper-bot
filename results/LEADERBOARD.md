# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 9:05 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 388 windows, 10601 settled trades, 62 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 11:15 PM | too few trades (196/200) |
| value_ev10 | 507 | 40.0 | 40.5 | $-209.23 | -4.1% | $790.77 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 894 | 50.3 | 49.8 | $-285.44 | -3.2% | $714.56 | -1.0 | done | can't tell from luck |
| value_ev5 | 748 | 41.7 | 42.1 | $-328.33 | -4.4% | $671.67 | -1.0 | done | can't tell from luck |
| trend_filter | 597 | 49.2 | 50.5 | $-397.88 | -6.7% | $602.12 | -1.7 | done | can't tell from luck |
| momentum_15m_0.10pct | 1065 | 49.2 | 49.7 | $-495.69 | -4.7% | $504.31 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 1065 | 50.8 | 52.1 | $-684.18 | -6.4% | $315.82 | -2.2 | done | losing for real |
| reversal_60m_0.30pct | 894 | 49.7 | 52.1 | $-758.17 | -8.5% | $241.83 | -2.7 | done | losing for real |
| coinflip | 1545 | 49.9 | 50.8 | $-836.57 | -5.4% | $163.43 | -2.2 | done | losing for real |
| momentum_5m_0.00pct | 1545 | 49.6 | 51.5 | $-1099.97 | -7.1% | $-99.97 | -2.9 | done | losing for real |
| always_up | 1545 | 46.1 | 50.7 | $-1952.29 | -12.6% | $-952.29 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2394 | 47.6 | 49.4 | $-1717.39 |
| ETH | 2661 | 47.8 | 48.9 | $-1805.54 |
| SOL | 2742 | 47.9 | 49.5 | $-2070.96 |
| XRP | 2804 | 48.7 | 49.2 | $-1480.81 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
