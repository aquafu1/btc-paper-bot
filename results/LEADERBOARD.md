# Paper trading leaderboard (FAKE money)

**Updated Sun Nov 15, 12:35 PM CT.** Running since Tue Nov 10, 3:15 PM CT: 450 windows, 12358 settled trades, 44 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 227 | 34.8 | 36.0 | $-152.39 | -6.7% | $847.61 | -0.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 1050 | 51.3 | 50.0 | $-179.67 | -1.7% | $820.33 | -0.6 | done | can't tell from luck |
| trend_filter | 710 | 50.1 | 50.7 | $-371.13 | -5.2% | $628.87 | -1.4 | done | can't tell from luck |
| value_ev10 | 582 | 38.5 | 40.1 | $-433.25 | -7.4% | $566.75 | -1.5 | done | can't tell from luck |
| value_ev5 | 862 | 40.8 | 41.8 | $-527.94 | -6.1% | $472.06 | -1.6 | done | can't tell from luck |
| momentum_15m_0.10pct | 1249 | 49.6 | 50.0 | $-551.07 | -4.4% | $448.93 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 1249 | 50.4 | 51.6 | $-839.50 | -6.7% | $160.50 | -2.5 | done | losing for real |
| coinflip | 1793 | 49.9 | 50.8 | $-990.66 | -5.5% | $9.34 | -2.4 | done | losing for real |
| reversal_60m_0.30pct | 1050 | 48.7 | 51.7 | $-1066.92 | -10.2% | $-66.92 | -3.5 | done | losing for real |
| momentum_5m_0.00pct | 1793 | 49.6 | 51.5 | $-1325.21 | -7.4% | $-325.21 | -3.2 | done | losing for real |
| always_up | 1793 | 45.8 | 50.5 | $-2365.67 | -13.2% | $-1365.67 | -5.7 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 2788 | 47.5 | 49.3 | $-2261.04 |
| ETH | 3105 | 47.9 | 48.8 | $-2117.84 |
| SOL | 3218 | 47.6 | 49.3 | $-2520.33 |
| XRP | 3247 | 48.4 | 49.2 | $-1904.20 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
