# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 9:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 390 windows, 10696 settled trades, 28 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 196 | 37.2 | 36.6 | $-26.95 | -1.4% | $973.05 | -0.1 | Sat 11:45 PM | too few trades (196/200) |
| value_ev10 | 509 | 40.3 | 40.5 | $-184.20 | -3.6% | $815.80 | -0.7 | done | can't tell from luck |
| momentum_60m_0.30pct | 905 | 50.6 | 49.8 | $-226.32 | -2.5% | $773.68 | -0.8 | done | can't tell from luck |
| value_ev5 | 755 | 41.9 | 42.2 | $-310.65 | -4.1% | $689.35 | -1.0 | done | can't tell from luck |
| trend_filter | 606 | 49.8 | 50.5 | $-318.76 | -5.3% | $681.24 | -1.3 | done | can't tell from luck |
| momentum_15m_0.10pct | 1076 | 49.4 | 49.7 | $-436.57 | -4.1% | $563.43 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 1076 | 50.6 | 52.1 | $-741.04 | -6.9% | $258.96 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 905 | 49.4 | 52.2 | $-815.03 | -9.0% | $184.97 | -2.8 | done | losing for real |
| coinflip | 1556 | 49.7 | 50.8 | $-881.21 | -5.7% | $118.79 | -2.3 | done | losing for real |
| momentum_5m_0.00pct | 1556 | 49.9 | 51.5 | $-1005.31 | -6.5% | $-5.31 | -2.6 | done | losing for real |
| always_up | 1556 | 46.3 | 50.7 | $-1893.17 | -12.2% | $-893.17 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2419 | 47.7 | 49.4 | $-1651.59 |
| ETH | 2687 | 47.9 | 48.9 | $-1724.28 |
| SOL | 2769 | 48.0 | 49.5 | $-2054.77 |
| XRP | 2821 | 48.8 | 49.2 | $-1408.58 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
