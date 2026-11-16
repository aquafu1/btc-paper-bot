# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 2:35 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 506 windows, 13945 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 264 | 34.5 | 35.5 | $-178.91 | -6.8% | $821.09 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1182 | 51.1 | 49.8 | $-191.40 | -1.6% | $808.60 | -0.6 | done | can't tell from luck |
| value_ev10 | 658 | 38.1 | 39.7 | $-490.51 | -7.5% | $509.49 | -1.6 | done | can't tell from luck |
| trend_filter | 817 | 49.6 | 50.7 | $-538.44 | -6.6% | $461.56 | -1.9 | done | can't tell from luck |
| momentum_15m_0.10pct | 1410 | 49.7 | 49.6 | $-558.33 | -4.0% | $441.67 | -1.5 | done | can't tell from luck |
| value_ev5 | 974 | 40.0 | 41.5 | $-693.88 | -7.1% | $306.12 | -1.9 | done | can't tell from luck |
| reversal_15m_0.10pct | 1410 | 50.3 | 51.6 | $-941.41 | -6.7% | $58.59 | -2.6 | done | losing for real |
| coinflip | 2016 | 50.0 | 50.7 | $-1071.84 | -5.3% | $-71.84 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1182 | 48.9 | 51.4 | $-1090.28 | -9.2% | $-90.28 | -3.2 | done | losing for real |
| momentum_5m_0.00pct | 2016 | 49.6 | 51.6 | $-1522.10 | -7.6% | $-522.10 | -3.5 | done | losing for real |
| always_up | 2016 | 46.4 | 50.1 | $-2324.92 | -11.5% | $-1324.92 | -5.3 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3150 | 47.4 | 49.2 | $-2512.34 |
| ETH | 3484 | 48.0 | 48.7 | $-2249.93 |
| SOL | 3638 | 47.6 | 49.0 | $-2737.24 |
| XRP | 3673 | 48.3 | 48.7 | $-2102.50 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
