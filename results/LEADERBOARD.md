# Paper trading leaderboard (FAKE money)

**Updated Sat Nov 14, 4:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 368 windows, 9952 settled trades, 61 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 189 | 38.1 | 36.4 | $+15.78 | +0.8% | $1015.78 | +0.1 | Sat 9:30 PM | too few trades (189/200) |
| value_ev10 | 484 | 41.1 | 40.4 | $-76.39 | -1.6% | $923.61 | -0.3 | done | can't tell from luck |
| value_ev5 | 715 | 42.4 | 42.1 | $-206.26 | -2.9% | $793.74 | -0.7 | done | can't tell from luck |
| trend_filter | 552 | 48.7 | 50.5 | $-423.22 | -7.7% | $576.78 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 821 | 49.2 | 49.7 | $-429.36 | -5.2% | $570.64 | -1.5 | done | can't tell from luck |
| reversal_15m_0.10pct | 989 | 51.5 | 52.1 | $-512.29 | -5.2% | $487.71 | -1.7 | done | can't tell from luck |
| reversal_60m_0.30pct | 821 | 50.8 | 52.1 | $-516.24 | -6.3% | $483.76 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 989 | 48.5 | 49.6 | $-565.24 | -5.7% | $434.76 | -1.8 | done | can't tell from luck |
| coinflip | 1464 | 49.9 | 50.8 | $-777.89 | -5.3% | $222.11 | -2.1 | done | losing for real |
| momentum_5m_0.00pct | 1464 | 49.6 | 51.6 | $-1056.59 | -7.2% | $-56.59 | -2.9 | done | losing for real |
| always_up | 1464 | 45.8 | 50.8 | $-1926.53 | -13.2% | $-926.53 | -5.2 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2236 | 47.4 | 49.3 | $-1741.39 |
| ETH | 2503 | 47.7 | 48.9 | $-1729.01 |
| SOL | 2579 | 48.1 | 49.4 | $-1778.53 |
| XRP | 2634 | 48.9 | 49.1 | $-1225.31 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
