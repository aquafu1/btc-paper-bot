# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 1:45 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 503 windows, 13841 settled trades, 73 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 256 | 34.0 | 35.5 | $-211.93 | -8.3% | $788.07 | -1.0 | done | can't tell from luck |
| momentum_60m_0.30pct | 1173 | 51.0 | 49.9 | $-263.08 | -2.2% | $736.92 | -0.8 | done | can't tell from luck |
| value_ev10 | 648 | 38.0 | 39.8 | $-533.29 | -8.2% | $466.71 | -1.7 | done | can't tell from luck |
| trend_filter | 813 | 49.4 | 50.8 | $-587.73 | -7.2% | $412.27 | -2.1 | done | losing for real |
| momentum_15m_0.10pct | 1401 | 49.7 | 49.7 | $-603.33 | -4.3% | $396.67 | -1.6 | done | can't tell from luck |
| value_ev5 | 964 | 39.9 | 41.6 | $-736.66 | -7.6% | $263.34 | -2.0 | done | losing for real |
| reversal_15m_0.10pct | 1401 | 50.3 | 51.5 | $-920.70 | -6.6% | $79.30 | -2.5 | done | losing for real |
| coinflip | 2004 | 50.1 | 50.7 | $-1025.17 | -5.1% | $-25.17 | -2.3 | done | losing for real |
| reversal_60m_0.30pct | 1173 | 49.0 | 51.3 | $-1042.75 | -8.9% | $-42.75 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 2004 | 49.6 | 51.6 | $-1546.24 | -7.7% | $-546.24 | -3.6 | done | losing for real |
| always_up | 2004 | 46.3 | 50.2 | $-2393.42 | -11.9% | $-1393.42 | -5.5 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3124 | 47.3 | 49.3 | $-2606.63 |
| ETH | 3461 | 48.0 | 48.7 | $-2350.16 |
| SOL | 3611 | 47.7 | 49.1 | $-2672.11 |
| XRP | 3645 | 48.2 | 48.8 | $-2235.38 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
