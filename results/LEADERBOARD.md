# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 16, 2:50 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 555 windows, 15393 settled trades, 55 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| momentum_60m_0.30pct | 1310 | 51.2 | 49.6 | $-258.15 | -2.0% | $741.85 | -0.7 | done | can't tell from luck |
| value_ev20 | 305 | 33.1 | 35.2 | $-345.92 | -11.3% | $654.08 | -1.5 | done | can't tell from luck |
| trend_filter | 891 | 50.5 | 51.0 | $-489.63 | -5.5% | $510.37 | -1.7 | done | can't tell from luck |
| value_ev10 | 730 | 37.1 | 39.3 | $-742.65 | -10.2% | $257.35 | -2.3 | done | losing for real |
| momentum_15m_0.10pct | 1563 | 49.4 | 49.8 | $-829.24 | -5.3% | $170.76 | -2.1 | done | losing for real |
| value_ev5 | 1085 | 39.6 | 41.1 | $-877.77 | -8.1% | $122.23 | -2.3 | done | losing for real |
| reversal_15m_0.10pct | 1563 | 50.6 | 51.1 | $-918.22 | -5.9% | $81.78 | -2.4 | done | losing for real |
| coinflip | 2212 | 49.9 | 50.5 | $-1252.03 | -5.7% | $-252.03 | -2.7 | done | losing for real |
| reversal_60m_0.30pct | 1310 | 48.8 | 51.2 | $-1292.48 | -9.9% | $-292.48 | -3.7 | done | losing for real |
| momentum_5m_0.00pct | 2212 | 50.3 | 51.8 | $-1537.74 | -7.0% | $-537.74 | -3.4 | done | losing for real |
| always_up | 2212 | 46.8 | 49.9 | $-2383.66 | -10.8% | $-1383.66 | -5.1 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 3477 | 47.5 | 49.2 | $-2776.67 |
| ETH | 3837 | 47.9 | 48.6 | $-2767.24 |
| SOL | 4017 | 47.7 | 48.7 | $-3062.80 |
| XRP | 4062 | 48.5 | 48.6 | $-2320.78 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
