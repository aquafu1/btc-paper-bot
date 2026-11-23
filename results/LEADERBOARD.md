# Paper trading leaderboard (FAKE money)

**Updated Mon Nov 23, 1:05 AM CT.** Running since Tue Nov 10, 3:15 PM CT: 1172 windows, 32413 settled trades, 48 waiting for results. Coins: BTC, ETH, SOL, XRP.

Each strategy: $1000 fake bankroll, $10 per trade, bought ~20s after each 15-min window opens at the real Polymarket order-book price, with Polymarket's real fee, settled by Polymarket's official result.

| Strategy | Trades | Win % | Break-even % | P&L | ROI | Bankroll | z | Hits 200 | Verdict |
|---|---|---|---|---|---|---|---|---|---|
| value_ev20 | 624 | 35.1 | 35.3 | $-315.19 | -5.1% | $684.81 | -1.0 | done | can't tell from luck |
| value_ev10 | 1533 | 38.6 | 39.2 | $-761.76 | -5.0% | $238.24 | -1.6 | done | can't tell from luck |
| reversal_15m_0.10pct | 3251 | 50.8 | 50.4 | $-1024.48 | -3.2% | $-24.48 | -1.8 | done | can't tell from luck |
| momentum_60m_0.30pct | 2735 | 49.7 | 49.4 | $-1164.20 | -4.3% | $-164.20 | -2.2 | done | losing for real |
| value_ev5 | 2321 | 40.3 | 41.1 | $-1218.24 | -5.2% | $-218.24 | -2.1 | done | losing for real |
| trend_filter | 1920 | 49.0 | 50.5 | $-1529.13 | -8.0% | $-529.13 | -3.6 | done | losing for real |
| reversal_60m_0.30pct | 2735 | 50.3 | 51.1 | $-1708.51 | -6.2% | $-708.51 | -3.4 | done | losing for real |
| momentum_15m_0.10pct | 3251 | 49.2 | 50.2 | $-1974.81 | -6.1% | $-974.81 | -3.5 | done | losing for real |
| coinflip | 4681 | 50.1 | 50.2 | $-2102.88 | -4.5% | $-1102.88 | -3.1 | done | losing for real |
| momentum_5m_0.00pct | 4681 | 50.1 | 51.4 | $-2922.66 | -6.2% | $-1922.66 | -4.4 | done | losing for real |
| always_up | 4681 | 47.8 | 49.3 | $-3404.53 | -7.3% | $-2404.53 | -4.9 | done | losing for real |

## By coin (all strategies)

| Coin | Trades | Win % | Break-even % | P&L |
|---|---|---|---|---|
| BTC | 7435 | 48.2 | 49.0 | $-3907.37 |
| ETH | 8040 | 48.1 | 48.4 | $-4761.07 |
| SOL | 8427 | 48.1 | 48.4 | $-4443.36 |
| XRP | 8511 | 48.1 | 48.2 | $-5014.60 |

**How to read this:** a strategy makes money only if **Win % beats Break-even %**. Ignore anything under 200 trades. It should also clearly beat `coinflip` (random picks). **z** = how many standard errors the average profit is above zero; "real edge?" needs z of 2 or more, and even then let it keep running before trusting it. The 4 coins usually move together, so a strategy's trades in the same window aren't fully independent.

Older test trades (Nov 9-10, entered 6-10 min late with a guessed fee) are kept in `archive_v1_trades.csv` and left out of these stats.
