# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 1:30 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 406 windows, 11120 settled trades, 43 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 202 | 36.1 | 36.5 | $-86.95 | -4.3% | $913.05 | -0.5 | done | can't tell from luck |
| momentum_60m_0.30pct | 948 | 51.1 | 49.9 | $-174.71 | -1.8% | $825.29 | -0.6 | done | can't tell from luck |
| value_ev10 | 523 | 40.2 | 40.5 | $-214.41 | -4.1% | $785.59 | -0.8 | done | can't tell from luck |
| trend_filter | 626 | 50.2 | 50.6 | $-305.23 | -4.9% | $694.77 | -1.2 | done | can't tell from luck |
| value_ev5 | 785 | 41.9 | 42.2 | $-323.76 | -4.1% | $676.24 | -1.0 | done | can't tell from luck |
| momentum_15m_0.10pct | 1120 | 49.6 | 49.9 | $-471.06 | -4.2% | $528.94 | -1.4 | done | can't tell from luck |
| reversal_15m_0.10pct | 1120 | 50.4 | 51.9 | $-751.99 | -6.7% | $248.01 | -2.4 | done | losing for real |
| coinflip | 1616 | 50.1 | 50.9 | $-813.04 | -5.0% | $186.96 | -2.1 | done | losing for real |
| reversal_60m_0.30pct | 948 | 48.9 | 52.0 | $-907.29 | -9.6% | $92.71 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 1616 | 49.8 | 51.6 | $-1098.83 | -6.8% | $-98.83 | -2.8 | done | losing for real |
| always_up | 1616 | 45.7 | 50.7 | $-2129.94 | -13.2% | $-1129.94 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2511 | 47.7 | 49.5 | $-1769.51 |
| ETH | 2794 | 47.9 | 48.9 | $-1769.86 |
| SOL | 2876 | 47.9 | 49.5 | $-2211.93 |
| XRP | 2939 | 48.9 | 49.3 | $-1525.89 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
