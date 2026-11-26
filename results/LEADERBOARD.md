# Paper trading leaderboard (FAKE money)

**Updated Wed Nov 25, 7:00 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 1436 windows, 36616 settled trades, 436 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 740 | 34.5 | 35.3 | $-533.47 | -7.2% | $466.53 | -1.5 | done | can't tell from luck |
| value_ev10 | 1780 | 38.8 | 39.1 | $-821.03 | -4.6% | $178.97 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3655 | 50.9 | 50.0 | $-993.65 | -2.7% | $6.35 | -1.6 | done | can't tell from luck |
| value_ev5 | 2682 | 40.5 | 41.1 | $-1305.48 | -4.9% | $-305.48 | -2.1 | done | losing for real |
| momentum_60m_0.30pct | 3072 | 49.2 | 49.3 | $-1528.96 | -5.0% | $-528.96 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 3072 | 50.8 | 51.0 | $-1568.10 | -5.1% | $-568.10 | -2.9 | done | losing for real |
| trend_filter | 2174 | 48.5 | 50.3 | $-1900.11 | -8.7% | $-900.11 | -4.2 | done | losing for real |
| coinflip | 5262 | 50.1 | 50.0 | $-2205.35 | -4.2% | $-1205.35 | -3.1 | done | losing for real |
| momentum_15m_0.10pct | 3655 | 49.1 | 50.2 | $-2264.08 | -6.2% | $-1264.08 | -3.8 | done | losing for real |
| momentum_5m_0.00pct | 5262 | 50.2 | 51.3 | $-3270.77 | -6.2% | $-2270.77 | -4.6 | done | losing for real |
| always_up | 5262 | 47.9 | 49.2 | $-3616.56 | -6.9% | $-2616.56 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 9304 | 48.1 | 48.7 | $-4901.84 |
| ETH | 10002 | 48.0 | 48.0 | $-5521.48 |
| SOL | 8627 | 48.3 | 48.4 | $-4336.33 |
| XRP | 8683 | 48.1 | 48.2 | $-5247.90 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
