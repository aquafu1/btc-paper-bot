# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 18, 6:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 715 windows, 19703 settled trades, 63 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 376 | 33.8 | 34.8 | $-284.03 | -7.6% | $715.97 | -1.1 | done | can't tell from luck |
| momentum_60m_0.30pct | 1656 | 50.2 | 49.5 | $-512.73 | -3.1% | $487.27 | -1.3 | done | can't tell from luck |
| reversal_15m_0.10pct | 2017 | 51.6 | 50.8 | $-512.80 | -2.5% | $487.20 | -1.1 | done | can't tell from luck |
| value_ev10 | 906 | 38.2 | 39.0 | $-552.57 | -6.1% | $447.43 | -1.5 | done | can't tell from luck |
| value_ev5 | 1366 | 40.8 | 41.0 | $-608.08 | -4.5% | $391.92 | -1.4 | done | can't tell from luck |
| trend_filter | 1153 | 50.3 | 50.9 | $-644.74 | -5.6% | $355.26 | -1.9 | done | can't tell from luck |
| coinflip | 2852 | 50.2 | 50.3 | $-1209.33 | -4.2% | $-209.33 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1656 | 49.8 | 51.3 | $-1268.26 | -7.7% | $-268.26 | -3.2 | done | losing for real |
| momentum_15m_0.10pct | 2017 | 48.4 | 50.0 | $-1428.31 | -7.1% | $-428.31 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2852 | 51.1 | 51.8 | $-1439.80 | -5.0% | $-439.80 | -2.8 | done | losing for real |
| always_up | 2852 | 47.3 | 49.5 | $-2455.41 | -8.6% | $-1455.41 | -4.6 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 4463 | 48.2 | 49.0 | $-2691.59 |
| ETH | 4902 | 48.3 | 48.5 | $-2830.72 |
| SOL | 5140 | 48.2 | 48.7 | $-2961.98 |
| XRP | 5198 | 48.6 | 48.4 | $-2431.77 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
