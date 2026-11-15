# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 9:20 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 437 windows, 12039 settled trades, 53 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 220 | 34.5 | 36.1 | $-178.23 | -8.1% | $821.77 | -0.9 | done | can't tell from luck |
| momentum_60m_0.30pct | 1027 | 51.0 | 49.9 | $-202.70 | -2.0% | $797.30 | -0.6 | done | can't tell from luck |
| trend_filter | 694 | 50.0 | 50.5 | $-355.51 | -5.1% | $644.49 | -1.4 | done | can't tell from luck |
| value_ev10 | 566 | 38.9 | 40.2 | $-393.63 | -7.0% | $606.37 | -1.4 | done | can't tell from luck |
| value_ev5 | 844 | 41.1 | 41.9 | $-489.11 | -5.8% | $510.89 | -1.5 | done | can't tell from luck |
| momentum_15m_0.10pct | 1219 | 49.5 | 50.0 | $-549.56 | -4.5% | $450.44 | -1.6 | done | can't tell from luck |
| coinflip | 1741 | 50.4 | 50.8 | $-819.01 | -4.7% | $180.99 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 1219 | 50.5 | 51.7 | $-822.26 | -6.7% | $177.74 | -2.5 | done | losing for real |
| reversal_60m_0.30pct | 1027 | 49.0 | 51.9 | $-1006.12 | -9.8% | $-6.12 | -3.3 | done | losing for real |
| momentum_5m_0.00pct | 1741 | 49.7 | 51.5 | $-1242.29 | -7.1% | $-242.29 | -3.1 | done | losing for real |
| always_up | 1741 | 46.0 | 50.5 | $-2216.46 | -12.7% | $-1216.46 | -5.4 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2715 | 47.5 | 49.3 | $-2104.52 |
| ETH | 3031 | 48.0 | 48.8 | $-1924.88 |
| SOL | 3123 | 47.8 | 49.3 | $-2458.84 |
| XRP | 3170 | 48.6 | 49.2 | $-1786.61 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
